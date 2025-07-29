<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-green-700 px-4 py-3 shadow sticky top-0 z-10">
      <div class="max-w-5xl mx-auto flex gap-5 items-center">
        <router-link
          to="/"
          class="text-white font-bold text-xl tracking-wider mr-6"
          >Теннис</router-link
        >
        <router-link
          to="/news"
          class="text-white hover:text-yellow-300 transition"
          >Новости</router-link
        >
        <router-link
          to="/tournaments"
          class="text-white hover:text-yellow-300 transition"
          >Турниры</router-link
        >
        <router-link
          to="/players"
          class="text-white hover:text-yellow-300 transition"
          >Игроки</router-link
        >
        <router-link
          to="/matches"
          class="text-white hover:text-yellow-300 transition"
          >Матчи</router-link
        >
      </div>
    </nav>
    <main class="max-w-5xl mx-auto px-4 py-8">
      <router-view />
    </main>
  </div>
</template>
