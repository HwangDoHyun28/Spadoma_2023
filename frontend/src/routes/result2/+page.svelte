<script>
    import { Input, Label, Helper } from "flowbite-svelte";
    import { Button, Spinner } from "flowbite-svelte";
    import { Select } from "flowbite-svelte";
    import {
      Table,
      TableBody,
      TableBodyCell,
      TableBodyRow,
      TableHead,
      TableHeadCell,
      Checkbox,
      TableSearch,
    } from "flowbite-svelte";
    let selected1;
    let dimension = [
      { value: "flag", name: "flag" },
      { value: "prism", name: "prism" },
      { value: "ocean", name: "ocean" },
      { value: "gist_earth", name: "gist_earth" },
      { value: "terrain", name: "terrain" },
      { value: "gist_stern", name: "gist_stern" },
      { value: "gnuplot", name: "gnuplot" },
      { value: "gnuplot2", name: "gnuplot2" },
      { value: "CMRmap", name: "CMRmap" },
      { value: "cubehelix", name: "cubehelix" },
      { value: "brg", name: "brg" },
      { value: "gist_rainbow", name: "gist_rainbow" },
      { value: "rainbow", name: "rainbow" },
      { value: "jet", name: "jet" },
      { value: "turbo", name: "turbo" },
      { value: "nipy_spectral", name: "nipy_spectral" },
      { value: "gist_ncar", name: "gist_ncar" },
    ];
  </script>
  
  <div class="rounded-lg border mx-10 px-20 py-10 bg-white">
    <div class="mt-5">
      <p class="text-5xl text-teal-600 font-medium my-5">Analysis</p>
      <div class="flex">
        <div>
          <p class="mt-5 text-3xl text-spadoma4 font-medium">Result</p>
          <p class="mt-5 text-spadoma3 text-base font-normal">Color Palette</p>
          <Select
            id="dimension"
            class="mt-2 text-slate-500"
            bind:value={selected1}
            placeholder=""
          >
            <option selected value="all">Default</option>
  
            {#each dimension as { value, name }}
              <option {value}>{name}</option>
            {/each}
          </Select>
          <div class="flex mt-6">
            <div class="mt-0">
              <Checkbox class="checked:bg-yellow-300 focus:ring-white" />
            </div>
            <p class="ml-5 text-teal-500 text-base font-normal">Coordinates</p>
          </div>
          <div class="flex mt-6">
            <div class="mt-0">
              <Checkbox class="checked:bg-yellow-300 focus:ring-white" />
            </div>
            <p class="ml-5 text-teal-500 text-base font-normal">Domain</p>
          </div>
          <div class="flex mt-6">
            <div clss="mt-0">
              <Checkbox class="checked:bg-yellow-300 focus:ring-white" />
            </div>
            <p class="ml-5 text-teal-500 text-base font-normal">Legend</p>
          </div>
        </div>
        <div>
            <img
            src="result_fig.svg"
            class="ml-32 mt-5 place-content-center"
            alt="SPADOMA Logo"/>
            <div class="-mt-10 ml-10 flex bg-teal-0">
                <div class="ml-32 mr-80 text-right bg-teal-0">
                    <Button
                    href="/analysis"
                    class="py-3 px-8 mt-16 text-xl font-medium bg-teal-500 hover:bg-teal-400 focus:ring-teal-300"
                    >Retry</Button
                    >
                </div>
                <div class="ml-72 text-right font-medium">
                    <Button
                    class="py-3 px-8 mt-16 text-xl font-medium bg-yellow-300 hover:bg-yellow-200 focus:ring-yellow-100"
                    >Save</Button
                    >
                </div>
            </div>
        </div>
      </div>
    </div>
    <div class="mt-10 -mb-10 ml-0 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center">
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
  