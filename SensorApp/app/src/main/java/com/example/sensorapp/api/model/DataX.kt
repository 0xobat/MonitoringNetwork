package com.example.sensorapp.api.model


import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class DataX(
    @Json(name = "Soil Moisture")
    val soilMoisture: String,
    @Json(name = "Temperature")
    val temperature: String,
    @Json(name = "Time")
    val time: String
)