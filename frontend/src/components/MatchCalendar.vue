<template>
  <div class="flex flex-col gap-4">
    <div
      v-for="match in limitedMatches"
      :key="match.id"
      class="bg-white rounded-xl shadow p-4"
    >
      <div class="flex items-center gap-2 mb-1">
        <span class="text-xs text-gray-400">{{ formatDate(match.date) }}</span>
        <span
          class="ml-auto px-2 py-0.5 rounded text-xs"
          :class="
            match.score
              ? 'bg-green-100 text-green-700'
              : 'bg-gray-200 text-gray-600'
          "
        >
          {{ match.score ? "Завершён" : "Запланирован" }}
        </span>
      </div>
      <div class="text-center">
        <span class="text-blue-700 font-semibold"
          >{{ match.player1_first_name }} {{ match.player1_last_name }}</span
        >
        <span class="text-gray-400"> vs </span>
        <span class="text-blue-700 font-semibold"
          >{{ match.player2_first_name }} {{ match.player2_last_name }}</span
        >
      </div>
      <div class="text-center text-gray-500 text-sm">
        <span
          >Турнир: <b>{{ match.tournament_name }}</b></span
        >
      </div>
      <div v-if="match.score" class="text-center mt-1 text-sm">
        Счёт: <b>{{ match.score }}</b>
      </div>
      <div
        v-if="match.winner_first_name"
        class="text-green-700 font-semibold text-center mt-1 text-sm"
      >
        Победитель: {{ match.winner_first_name }} {{ match.winner_last_name }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
const props = defineProps({ limit: { type: Number, default: null } });

const matchList = ref([]);

const limitedMatches = computed(() =>
  props.limit ? matchList.value.slice(0, props.limit) : matchList.value
);

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleString();
}

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/matches/");
  let data = await res.json();
  console.log("Fetched matches:", data);

  matchList.value = data.map((match) => ({
    ...match,
    tournament_name: match.tournament?.name ?? "",
    player1_first_name: match.player1?.first_name ?? "",
    player1_last_name: match.player1?.last_name ?? "",
    player2_first_name: match.player2?.first_name ?? "",
    player2_last_name: match.player2?.last_name ?? "",
    winner_first_name: match.winner?.first_name ?? "",
    winner_last_name: match.winner?.last_name ?? "",
  }));
});
</script>
