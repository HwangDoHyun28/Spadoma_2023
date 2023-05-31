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

from tempfile import NamedTemporaryFile
from typing import IO
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173" "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보"}


@app.post("/file/size")
def get_filesize(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/file/info")
def get_file_info(file: UploadFile = File(...)):
    return {
        "content_type": file.content_type,
        "filename": file.filename
    }
    
    
async def save_file(file: IO):
    # s3 업로드라고 생각해 봅시다. delete=True(기본값)이면
    # 현재 함수가 닫히고 파일도 지워집니다.
    with NamedTemporaryFile("wb", delete=False) as tempfile:
        tempfile.write(file.read())
        return tempfile.name


@app.post("/file/store")
async def store_file(file: UploadFile = File(...)):
    path = await save_file(file.file)
    return {"filepath": path}


@app.get("/spadoma")
def SPADOMA(dimension="3D", n_clusters='20' , merge_thres = 0.8, merge_remote = True, norm_thres = 1):
    if dimension == "3D":
        df = pd.read_csv('cluster_table.csv')
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