<script lang="ts" setup>
import type { CreateUser, User } from '@/userDTO'
import { ref, watch, computed } from 'vue'

// Define props with types
const props = defineProps<{
    modelValue: boolean
    user: User | null
}>()

const isEdit = ref<boolean>(props.user !== null ? true : false)

// Define emitted events with types
const emit = defineEmits<{
    (e: 'update:modelValue', value: boolean): void
    (e: 'save', userData: User): void
    (e: 'create', userData: CreateUser): void
}>()

// Local copy of the dialog visibility
const localVisible = ref<boolean>(props.modelValue)

// Default user values for creation
const defaultUser: User = {
    username: '',
    password: '',
    roles: [],
    preferences: { timezone: '' },
    active: true,
    created_ts: Date.now(),
    updated_at: Date.now(),
}

// Local copy of user data (for both create and edit)
const localUser = ref<User>(
    props.user ? JSON.parse(JSON.stringify(props.user)) : { ...defaultUser },
)

// List of available roles (this could be fetched from an API)
const allRoles = ref<string[]>(['is_user_admin', 'is_user_manager', 'is_user_editor'])

// Computed property to determine edit mode
const isEditMode = computed<boolean>(() => props.user !== null && props.user._id !== undefined)

// Watch for external changes to the modelValue
watch(
    () => props.modelValue,
    (val) => {
        localVisible.value = val
        if (val && props.user) {
            localUser.value = JSON.parse(JSON.stringify(props.user))
        } else if (val) {
            localUser.value = { ...defaultUser }
        }
    },
    { immediate: true },
)

// Emit changes when localVisible changes
watch(localVisible, (val) => {
    emit('update:modelValue', val)
})

function close(): void {
    localVisible.value = false
}

function submit(): void {
    if (isEdit.value) {
        emit('save', { ...localUser.value } as User)
    } else {
        const newUser = {
            username: localUser.value.username,
            password: localUser.value.password,
            roles: localUser.value.roles,
            preferences: localUser.value.preferences,
            active: true,
            created_ts: localUser.value.created_ts,
            updated_at: localUser.value.updated_at,
        } as CreateUser
        emit('create', newUser)
    }
    close()
}
</script>

<template>
    <v-dialog v-model="localVisible" max-width="600">
        <v-card>
            <v-card-title>
                <span class="text-h6">{{ isEditMode ? 'Edit User' : 'Create User' }}</span>
            </v-card-title>
            <v-card-text>
                <v-form ref="userForm" lazy-validation>
                    <v-text-field
                        v-model="localUser.username"
                        label="Username"
                        required
                    ></v-text-field>
                    <v-text-field
                        v-if="!isEditMode"
                        v-model="localUser.password"
                        label="Password"
                        type="password"
                        required
                    ></v-text-field>
                    <v-combobox
                        v-model="localUser.roles"
                        :items="allRoles"
                        label="Roles"
                        multiple
                        chips
                    ></v-combobox>
                    <v-text-field
                        v-model="localUser.preferences.timezone"
                        label="Timezone"
                    ></v-text-field>
                    <v-checkbox
                        v-model="localUser.active"
                        label="Active"
                        color="primary"
                        hide-details
                    ></v-checkbox>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text="button1" @click="close">Cancel</v-btn>
                <v-btn color="primary" text="button2" @click="submit"> Save </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
