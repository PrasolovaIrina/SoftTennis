<template>
  <div class="flex flex-col gap-4">
    <div
      v-for="player in limitedPlayers"
      :key="player.id"
      class="bg-white rounded-xl shadow p-4 flex items-center gap-4"
    >
      <img
        v-if="player.photo"
        :src="player.photo"
        alt="player photo"
        class="w-12 h-12 object-cover rounded-full border-2 border-blue-200"
      />
      <div>
        <div class="font-semibold">
          {{ player.first_name }} {{ player.last_name }}
        </div>
        <div class="text-xs text-gray-500">
          Рейтинг: <span class="font-bold">{{ player.rank }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
const props = defineProps({ top: { type: Number, default: null } });

const playerList = ref([]);

const limitedPlayers = computed(() =>
  props.top
    ? [...playerList.value].sort((a, b) => a.rank - b.rank).slice(0, props.top)
    : playerList.value
);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/players/");
  playerList.value = await res.json();
});
</script>
