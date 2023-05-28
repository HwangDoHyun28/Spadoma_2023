<script>
    import { Input, Label, Helper } from "flowbite-svelte";
    import { Fileupload, Button } from "flowbite-svelte";
    import { Select } from "flowbite-svelte";
  
    let selected1;
    let selected2;
    let dimension = [
      { value: "2d", name: "2D" },
      { value: "3d", name: "3D" },
    ];
    let remote = [
      { value: "T", name: "True" },
      { value: "F", name: "False" },
    ];
  
    let value;

    import { Dropdown, DropdownItem, Chevron, Radio } from 'flowbite-svelte'
    let group1="Select Dimension";
  
</script>

<form type="submit">
    <div class="rounded-lg border mx-10 px-20 py-10 bg-white">
        <div class="mt-5">
        <p class="text-5xl text-teal-600 font-medium my-5">Analysis</p>
        <p class="text-slate-400 text-lg font-normal">
            SPADOMA allows you to upload a file containing information for clustering
            and obtain the results of adjusting various parameters.
        </p>
        </div>
        <div class="mt-12 my-10">
        <p class="text-3xl text-teal-600 font-medium">Data</p>
        <p class="text-teal-500 text-spadoma3 font-normal mt-2">
            Upload a csv-formatted file containing cell types and coordinates
        </p>
        <Label class="w-32 mt-1 space-y-2 mb-2">
            <Fileupload class = "w-32 opacity-0" bind:value/>
        </Label>
        
        
        </div>
        <div class="flex -mt-[88px]">
        <div>
            <Button class="mt-3 bg-spadoma2 hover:bg-teal-400 text-base font-medium"
            >Select File</Button
            >
        </div>
        <div class="relative top-5 text-center">
            <Label class="text-slate-300 text-center text-base font-normal px-3 ml-0 mt-0">{value}</Label>
        </div>
        </div>
        <div>
        <p class="mt-16 text-3xl text-teal-600 font-medium">Parameter</p>
        <div class="flex">
            <div class="text-center">
            <p class="mt-2 text-spadoma3 text-base font-normal">
                Dimension(X, Y, or Z...)
            </p>
            
            <Select
                id="dimension"
                class="mt-2 text-teal-500 bg-inherit default:bg-spadoma1 focus:ring-white focus:border-spadoma1"
                bind:value={selected1}
                placeholder=""
            >
                <option class="bg-white hover:bg-spadoma1" selected value="all">Select Dimension</option>

                {#each dimension as { value, name } }
                <option class="bg-white hover:bg-spadoma1" {value}>{name}</option>
                {/each}
            </Select>
            </div>
            <div class="mt-2 text-slate-500 text-center mx-12">
            <p class="text-spadoma3 text-base font-normal">
                Number 0f Clusters(1~n)
            </p>
            <Input
                class="text-teal-500 mt-2 bg-inherit focus:ring-white focus:border-spadoma1"
                type="number"
                id="last_name"
                placeholder="Write Number"
                required
            />
            </div>
            <div class="mt-2 text-center">
            <p class="-ml-0 mx-5 text-spadoma3 text-base font-normal">Merge Threshold(0~1)</p>
            <Input
                class="text-teal-500 mt-2 bg-inherit focus:ring-white focus:border-spadoma1"
                type="number"
                id="last_name"
                placeholder="Write Threshold"
                required
            />
            </div>
            <div class="mt-2 text-center mx-12">
            <p class="text-spadoma3 text-base font-normal">
                Merge Remote(True/False)
            </p>
            <Select
                id="remote"
                class="mt-2 text-teal-500 bg-inherit focus:ring-white focus:border-spadoma1"
                bind:value={selected2}
                placeholder=""
            >
                <option selected value="all">Select True/False</option>

                {#each remote as { value, name }}
                <option {value}>{name}</option>
                {/each}
            </Select>
            </div>
            <div class="mx-5 mt-2 text-center">
            <p class="-ml-3 text-spadoma3 text-base font-normal">Norm Threshold(0~1)</p>
            <Input
                class="text-teal-500 mt-2 bg-inherit focus:ring-white focus:text-teal-500 focus:border-spadoma1"
                type="number"
                id="last_name"
                placeholder="Write Threshold"
                required
            />
            </div>
        </div>
        </div>

        <div class="text-center">
        <Button
            href="/loading"
            class="py-3 px-5 mt-16 text-xl font-medium bg-yellow-300 hover:bg-yellow-200 focus:ring-yellow-100"
            >Submit</Button
        >
        </div>
        <div class="mt-20 -mb-10 ml-0 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center">
        <Button type="submit" target="self"
        href="https://pnucolab.com/"
        class="-mt-96 ml-3 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center focus:ring-white">
            <img
            src="lab_tag.svg"
            alt="Tutorial Logo"
        />
        </Button>
        </div>
    </div>
</form>

  
  