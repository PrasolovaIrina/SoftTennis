<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <div
      v-for="news in newsList"
      :key="news.id"
      class="bg-white rounded-2xl shadow hover:shadow-lg transition p-6 flex flex-col"
    >
      <h3 class="text-xl font-bold mb-3">{{ news.title }}</h3>
      <img
        v-if="news.image"
        :src="news.image"
        alt="news image"
        class="rounded mb-3 h-44 object-cover w-full"
      />
      <p class="mb-4 text-gray-700 line-clamp-4">{{ news.content }}</p>
      <span class="text-xs text-gray-400 mt-auto">{{
        formatDate(news.published_at)
      }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const newsList = ref([]);
function formatDate(dateStr) {
  return new Date(dateStr).toLocaleString();
}
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/news/");
  newsList.value = await res.json();
});
</script>
