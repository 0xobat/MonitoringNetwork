package com.example.sensorapp.api.model


import com.example.sensorapp.api.model.DataX
import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class SensorData(
    @Json(name = "data")
    val `data`: List<DataX>
)