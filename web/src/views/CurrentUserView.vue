<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = route.params.id
</script>

<template>
    <div class="user-details">
        <h1>User Details</h1>
        <p>User ID: {{ userId }}</p>
    </div>
</template>
