<script>
  import { Input, Label, Helper } from "flowbite-svelte";
  import { ButtonGroup, Button } from "flowbite-svelte";
  import { Select } from "flowbite-svelte";
</script>

<div class="relative px-8">
  <img
    src="homefig.svg"
    class="mt-0 ml-1 h-max place-content-center"
    alt="Tutorial Logo"
  />
  <div class="place-content-center absolute inset-x-1/2 bottom-96">
    <div class="left-96">
      <Button
        href="/about"
        class="py-4 px-6 mt-12 -ml-10 text-xl font-semibold bg-yellow-300 hover:bg-yellow-200 focus:ring-yellow-100"
        >About</Button
      >
    </div>
  </div>
  <div class="-mt-10 ml-0 h-max bg-inherit hover:bg-inherit rounded-lg place-content-center">
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
