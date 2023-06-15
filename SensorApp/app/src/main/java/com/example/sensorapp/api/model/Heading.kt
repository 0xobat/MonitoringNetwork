package com.example.sensorapp.api.model


import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Heading(
    @Json(name = "data")
    val `data`: List<Data>
)