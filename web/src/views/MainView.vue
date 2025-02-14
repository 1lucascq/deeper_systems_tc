<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import UserDialog from '@/components/UserDialog.vue'
import type { CreateUserDTO, User } from '@/userDTO'
import { UserService } from '@/api/UserService'


const users = ref<User[]>([])
const headers = [
    { title: 'Username', key: 'username' },
    { title: 'Roles', key: 'roles' },
    { title: 'Timezone', key: 'preferences.timezone' },
    { title: 'Is Active?', key: 'active' },
    { title: 'Last Updated At', key: 'updated_at' },
    { title: 'Created At', key: 'created_ts' },
    { title: 'Actions', key: 'actions' },
]

// Dialog state management
const editCreateDialogVisible = ref<boolean>(false)
const selectedUser = ref<User | null>(null)
const deleteDialogVisible = ref<boolean>(false)
const userToDelete = ref<User | null>(null)

function openCreateDialog() {
    selectedUser.value = null
    editCreateDialogVisible.value = true
}

function openEditDialog(userId: string) {
    selectedUser.value = { ...users.value.find((u) => u._id === userId)! }
    editCreateDialogVisible.value = true
}

function confirmDelete(userId: string) {
    userToDelete.value = users.value.find((u) => u._id === userId)!
    deleteDialogVisible.value = true
}

async function saveUser(userData: User) {
    try {
        if (selectedUser.value) {
            await UserService.updateUser(selectedUser.value._id, userData)
            // Refresh users list
            users.value = await UserService.getUsers()
        }
        editCreateDialogVisible.value = false
    } catch (error) {
        console.error('Failed to update user:', error)
    }}

async function createUser(userData: CreateUserDTO) {
    console.log(userData)
    editCreateDialogVisible.value = false
}

async function deleteUser() {
    if (userToDelete.value) {
        users.value = users.value.filter((u) => u._id !== userToDelete.value!._id)
        deleteDialogVisible.value = false
    }
}

onMounted(async () => {
    try {
        users.value = await UserService.getUsers()
        console.log(users.value)
    } catch (error) {
        console.error('Failed to fetch users:', error)
    }
})

</script>

<template>
    <v-app>
        <v-container fluid>
            <v-data-table :items="users" :headers="headers" item-key="_id">
                <template v-slot:top>
                    <v-row>
                        <v-col cols="12">
                            <v-btn color="primary" @click="openCreateDialog"> Create User </v-btn>
                        </v-col>
                    </v-row>
                </template>
                <template v-slot:item="props">
                    <td>
                        <RouterLink :to="{ name: 'userDetails', params: { id: props.item._id } }">
                            {{ props.item.username }}
                        </RouterLink>
                    </td>
                    <td>{{ props.item.roles }}</td>
                    <td>{{ props.item.preferences.timezone }}</td>
                    <td>{{ props.item.active }}</td>
                    <td>{{ props.item.updated_at }}</td>
                    <td>{{ props.item.created_ts }}</td>
                    <td>
                        <v-icon
                            @click="openEditDialog(props.item._id!)"
                            class="mr-2"
                            color="primary"
                        >
                            mdi-pencil
                        </v-icon>
                        <v-icon @click="confirmDelete(props.item._id!)" color="red">
                            mdi-delete
                        </v-icon>
                    </td>
                </template>
            </v-data-table>

            <!-- Create/Edit User Dialog -->
            <UserDialog
                :model-value="editCreateDialogVisible"
                :user="selectedUser"
                @update:modelValue="(val) => (editCreateDialogVisible = val)"
                @save="saveUser"
                @create="createUser"
            />

            <!-- Delete Confirmation Dialog -->
            <v-dialog v-model="deleteDialogVisible" max-width="500">
                <v-card>
                    <v-card-title class="headline"> Confirm Delete </v-card-title>
                    <v-card-text>
                        Are you sure you want to delete user
                        <strong>{{ userToDelete?.username }}</strong
                        >?
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text="buttonM1" @click="deleteDialogVisible = false"> Cancel </v-btn>
                        <v-btn color="red" text="buttonM2" @click="deleteUser"> Delete </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-container>
    </v-app>
</template>

<style scoped>
td {
    padding-inline: 1rem;
}
</style>
