interface UserPreferences {
    timezone: string
}

export interface User {
    _id?: string
    username: string
    password: string
    roles: string[]
    preferences: UserPreferences
    updated_at: number
    active: boolean
    created_ts: number
}

export interface CreateUser {
    username: string
    password: string
    roles: string[]
    preferences: UserPreferences
    active: boolean
}
