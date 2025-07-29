<template>
  <div class="flex flex-col lg:flex-row gap-8">
    <!-- Центральная колонка с новостями -->
    <section class="flex-1">
      <h2 class="text-2xl font-bold mb-5">Новости</h2>
      <NewsList />
    </section>

    <!-- Правая колонка: календарь матчей и рейтинг игроков -->
    <aside class="w-full lg:w-96 flex flex-col gap-8">
      <div>
        <h2 class="text-xl font-semibold mb-3 text-center">Календарь матчей</h2>
        <MatchCalendar :limit="5" />
      </div>
      <div>
        <h2 class="text-xl font-semibold mb-3 text-center">Рейтинг игроков</h2>
        <PlayerList :top="5" />
      </div>
    </aside>
  </div>
</template>

<script setup>
import NewsList from "../components/NewsList.vue";
import MatchCalendar from "../components/MatchCalendar.vue";
import PlayerList from "../components/PlayerList.vue";
</script>
