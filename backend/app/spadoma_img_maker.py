import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from skimage import measure
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import radius_neighbors_graph
import leidenalg as la
import igraph as ig
from sklearn.neighbors import kneighbors_graph

import psycopg2
import pandas as pd
from sqlalchemy import create_engine 

SPADOMA_file = input()

# csv 데이터 로딩 후 컬럼 소문자로 변환
selloutData = pd.read_csv("./f{SPADOMA_file}.csv")

# 데이터베이스 접속 엔진 생성
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5173/postgres')    # localhost의 5173 포트를 Parallels에 설치된 PostgreSQL 5432 포트로 포트포워딩.

# 데이터 저장
resultname='spadoma_csv'
selloutData.to_sql(name=resultname, con=engine, index = False, if_exists='replace')











def SPADOMA(dimension, n_clusters, merge_thres = 0.8, merge_remote = True, norm_thres = 1):
    if dimension == "3D":
        df = pd.read_sql_query("select * from spadoma_csv", engine)
        #df = pd.read_csv('cluster_table.csv')
        df1 = df[['x', 'y', 'wb_cluster_label']].set_index('wb_cluster_label')
        df1['z'] = 0
        df1['x'] = df1['x'] - int(df1['x'].min()) + 1
        df1['y'] = df1['y'] - int(df1['y'].min()) + 1
        df1['z'] = df1['z'] - int(df1['z'].min())
        df1['x']= df1['x'].astype(int)
        df1['y']= df1['y'].astype(int)
        df1['z']= df1['z'].astype(int)

        gene_bin = {}
        sub_list = sorted(df1.index.unique())

        num = len(sub_list)
        for i in range(num):
            gene_bin[sub_list[i]] = i
        
        ct_idx_array = np.array([gene_bin[ct] for ct in df1.index])
        
        X = df1.to_numpy()
        neigh = NearestNeighbors(radius=100)
        neigh.fit(X)
        
        X,Y,Z = np.meshgrid(np.arange(0,5500,10),np.arange(0,2500,10), np.arange(0,10,10))
        grid_xyz = list(zip(X.ravel(), Y.ravel(), Z.ravel()))

        nbrs = neigh.radius_neighbors(grid_xyz, 100, return_distance=False)
        ct_bincount = [np.bincount(ct_idx_array[indices], minlength=len(gene_bin)) for indices in nbrs]
        ct_bincount = np.array(ct_bincount)

        norm_ct_bincount = preprocessing.normalize(ct_bincount, norm='l1')

        ct_bincount_10 = ct_bincount[ct_bincount.sum(axis=1) > 10]
        norm_ct_bincount_10 = preprocessing.normalize(ct_bincount_10, norm='l1')

        clustering_10 = AgglomerativeClustering(n_clusters, linkage='ward', metric='euclidean', compute_distances=True).fit(norm_ct_bincount_10)
        labels_predicted_10 = clustering_10.labels_ + 1

        mask_10 = np.zeros(ct_bincount.shape)
        mask_10 = np.where(ct_bincount.sum(axis=1) > 10, 1, 0)

        num = 0
        for i in range(len(mask_10)):
            if mask_10[i] == 1:
                mask_10[i] = labels_predicted_10[num]
                num+=1

        t10 = mask_10.reshape(250, 550, 1)

        plt.figure(figsize=[15, 10])
        plt.imshow(t10)
        plt.savefig('inferred_domains_plot.png')
    else:
        return 0
    
    return t10