package com.example.sensorapp.api

import android.preference.PreferenceActivity
import com.example.sensorapp.api.model.Heading
import com.google.gson.Gson
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.util.concurrent.TimeUnit
/*
fun getAPIData(urlIn: String): List<Heading> {
    val url = URL(urlIn)
    with(url.openConnection() as HttpURLConnection) {
        requestMethod = "GET"
        connectTimeout = 5000
        readTimeout = 5000
        connect()
        return BufferedReader(InputStreamReader(inputStream)).use {
            Gson().fromJson(it, Array<Heading>::class.java).toList()
        }
    }
}

 */
/*
interface APIService {
    @GET("dashboard")
    suspend fun getHeading(): Heading

}
*/