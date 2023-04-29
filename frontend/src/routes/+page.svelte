<script>
  import { Input, Label, Helper } from "flowbite-svelte";
  import { ButtonGroup, Button } from "flowbite-svelte";
  import { Select } from "flowbite-svelte";
</script>

<div class="relative">
  <img
    src="homefig.svg"
    class="mt-2 ml-16 h-max place-content-center"
    alt="Tutorial Logo"
  />
  <div class="absolute inset-x-1/2 bottom-96">
    <div class="left-96">
      <Button
        href="/about"
        class="py-3 px-5 mt-16 text-xl font-semibold bg-yellow-300 hover:bg-yellow-200"
        >About</Button
      >
    </div>
  </div>
</div>
