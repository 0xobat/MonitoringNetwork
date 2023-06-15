package com.example.sensorapp.api

import com.example.sensorapp.api.model.Heading
import retrofit2.Call
import retrofit2.http.GET

interface SoilSensorService {
    @GET("character/2")
    fun getHeading(): Call<Any>
}