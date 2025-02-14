<script lang="ts" setup>
import type { User } from '@/userDTO'
import { computed } from 'vue'

interface Props {
    modelValue: boolean
    user: User | null
}

interface Emits {
    (e: 'update:modelValue', value: boolean): void
    (e: 'confirm'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const dialogModel = computed({
    get: () => props.modelValue,
    set: (value: boolean) => emit('update:modelValue', value),
})

const closeDialog = () => {
    emit('update:modelValue', false)
}

const confirmDelete = () => {
    emit('confirm')
    closeDialog()
}
</script>

<template>
    <v-dialog v-model="dialogModel" max-width="500">
        <v-card>
            <v-card-title class="headline">Confirm Delete</v-card-title>
            <v-card-text>
                Are you sure you want to delete user
                <strong>{{ user?.username }}</strong
                >?
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text="Cancel" @click="closeDialog">Cancel</v-btn>
                <v-btn color="red" text="Delete" @click="confirmDelete">Delete</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
