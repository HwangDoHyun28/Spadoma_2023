<script>
  import { Input, Label, Helper } from "flowbite-svelte";
  import { Button } from "flowbite-svelte";
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

  let files;
</script>

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
    <div class="sr-only flex mt-1">
      <div>
        <Button class="mt-3 bg-spadoma3 hover:bg-teal-400 text-base font-medium focus:ring-teal-300"
          >Select File</Button
        >
      </div>
      <div class="relative top-5 text-center">
        <p
          class="relative text-center px-3 text-slate-300 text-base font-normal"
        >
          No files selected
        </p>
        
      </div>
    </div>
    <input type="file" placeholder="No files selected" class="mt-2 not-sr-only rounded-lg block w-full text-sm text-slate-300
    file:mr-4 file:py-2 file:px-4
    file:rounded-lg file:w-28 file:h-10
    file:text-base file:font-semibold
    file:text-center file:bg-spadoma4 file:text-white 
    hover:file:bg-spadoma3" bind:files/>
  
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
          class="mt-2 text-slate-500"
          bind:value={selected1}
          placeholder=""
        >
          <option selected value="all">Select Dimension</option>

          {#each dimension as { value, name }}
            <option {value}>{name}</option>
          {/each}
        </Select>
      </div>
      <div class="mt-2 text-slate-500 text-center mx-12">
        <p class="text-spadoma3 text-base font-normal">
          Number 0f Clusters(1~n)
        </p>
        <Input
          class="text-slate-400 mt-2"
          type="number"
          id="last_name"
          placeholder="Write Number"
          required
        />
      </div>
      <div class="mt-2 text-center">
        <p class="mx-5 text-spadoma3 text-base font-normal">Merge Threshold(0~1)</p>
        <Input
          class="text-slate-500 mt-2"
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
          class="mt-2 text-slate-500"
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
        <p class="text-spadoma3 text-base font-normal">Norm Threshold(0~1)</p>
        <Input
          class="text-slate-500 mt-2"
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
    <Button target="self"
    href="https://pnucolab.com/"
    class="-mt-96 ml-3 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center">
      <img
      src="lab_tag.svg"
      alt="Tutorial Logo"
    />
    </Button>
  </div>
</div>
