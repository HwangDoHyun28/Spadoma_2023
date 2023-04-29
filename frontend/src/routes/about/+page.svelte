<script>
  import { Input, Label, Helper } from "flowbite-svelte";
  import { Button } from "flowbite-svelte";
  import { Select } from "flowbite-svelte";
</script>

<div class="rounded-lg border mx-10 px-20 py-10 bg-white">
  <div class="mt-5">
    <p class="text-5xl text-teal-600 font-medium my-5">About</p>
    <p class="text-slate-400 text-lg font-normal">
      In SPADOMA, in order to eliminate the process of domain analysis
      corresponding each gene type to the coordinates one-on-one, we use the knn
      algorithm to make a mask and cluster each gene type without moving it. In
      addition, unlike algorithms that only consider x and y coordinates for
      existing two-dimensional data, it is a machine learning-based algorithm
      that can be applied to three-dimensional data by considering the z-axis.
    </p>
    <p class="mt-2 text-teal-500 text-xl font-normal">
      Enjoy the coolness of SPADOMA!
    </p>
  </div>
  <img
    src="aboutfig.svg"
    class="mt-10 place-content-center"
    alt="SPADOMA Logo"
  />
</div>
