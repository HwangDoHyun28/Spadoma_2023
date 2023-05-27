<script>
  import "../app.postcss";
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
  } from "flowbite-svelte";
  import { page } from "$app/stores";
</script>

<header class="px-8 border-b border-gray-200">
  <Navbar let:hidden let:toggle>
    <NavBrand href="/">
      <img
        src="logo.svg"
        class="pl-6 mr-4 -ml-4 h-14 sm:h-14"
        alt="SPADOMA Logo"
      />
    </NavBrand>
    <NavHamburger on:click={toggle} />
    <NavUl {hidden}>
      <NavLi
        id="home"
        href="/"
        class="block py-2 pl-3 pr-4 font-semibold text-base text-spadoma1 active:text-teal-500 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-teal-500 md:p-0 md:dark:hover:text-slate-300 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
        >Home</NavLi
      >
      <NavLi
        href="/about"
        class="block py-2 pl-3 pr-4 font-semibold text-base text-spadoma1 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-teal-500 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
        >About</NavLi
      >
      <NavLi
        href="/tutorial"
        class="block py-2 pl-3 pr-4 font-semibold text-base text-spadoma1 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-teal-500 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
        >Tutorial</NavLi
      >
      <NavLi
        href="/analysis"
        class="block py-2 pl-3 pr-4 font-semibold text-base text-spadoma1 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-teal-500 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
        >Analysis</NavLi
      >
    </NavUl>
  </Navbar>
</header>
<main class="bg-gray-100 py-5">
  <slot />
</main>
<footer class="mt-10">
  <hr />
  <div class="text-center py-5">
    <span class="text-sm text-gray-500">
      © 2023 SPADOMA. All rights reserved.
    </span>
  </div>
</footer>
