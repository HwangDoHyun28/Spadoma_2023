<script>
  import { Input, Label, Helper } from "flowbite-svelte";
  import { Button } from "flowbite-svelte";
  import { Svrollbar } from 'svrollbar';
  

</script>

<div class="rounded-lg border mx-10 px-20 py-10 bg-white">
  <div class="mt-5">
    <p class="text-5xl text-teal-600 font-medium my-5">Tutorial</p>
    <p class="text-slate-400 text-lg font-normal">
      Let's find out how to use the SPADOMA tool!
    </p>
  </div>
  <img
    src="tutorialfig.svg"
    class="mt-5 h-fit text-center"
    alt="Tutorial Logo"
  />
  <div class="mt-12 -mb-10 ml-0 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center">
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
