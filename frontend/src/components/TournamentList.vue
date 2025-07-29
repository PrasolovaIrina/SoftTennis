<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <div
      v-for="tournament in tournamentList"
      :key="tournament.id"
      class="bg-white rounded-2xl shadow hover:shadow-lg transition p-6 flex flex-col"
    >
      <div class="flex items-center gap-4 mb-3">
        <img
          v-if="tournament.logo"
          :src="tournament.logo"
          alt="logo"
          class="w-16 h-16 object-contain rounded"
        />
        <div>
          <h3 class="text-lg font-semibold">{{ tournament.name }}</h3>
          <p class="text-gray-400">{{ tournament.location }}</p>
        </div>
      </div>
      <p class="mb-1">
        <b>Сроки:</b> {{ tournament.start_date }} — {{ tournament.end_date }}
      </p>
      <p v-if="tournament.description" class="text-gray-700 mb-2">
        {{ tournament.description }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const tournamentList = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/tournaments/");
  tournamentList.value = await res.json();
});
</script>
