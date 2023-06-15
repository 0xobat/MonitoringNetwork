package com.example.sensorapp


import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.ui.Modifier
import com.example.sensorapp.api.SoilSensorService
import com.example.sensorapp.ui.theme.SensorAppTheme
import com.squareup.moshi.Moshi
import okhttp3.OkHttpClient
import okhttp3.Request
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.moshi.MoshiConverterFactory
import java.io.IOException


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SensorAppTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colors.background
                ) {
                    //MainScreen()
                }
            }
        }
        /*
        val moshi = Moshi.Builder()
            .addLast(com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory())
            .build()
        val retrofit = Retrofit.Builder()
            .baseUrl("http://127.0.0.1:8000/")
            .addConverterFactory(MoshiConverterFactory.create(moshi))
            .build()

        val soilSensorService: SoilSensorService = retrofit.create(SoilSensorService::class.java)

        soilSensorService.getHeading().enqueue(object : Callback<Any> {
            override fun onResponse(call: Call<Any>, response: Response<Any>) {
                Log.i("MainActivity", response.toString())
            }

            override fun onFailure(call: Call<Any>, t: Throwable) {
                Log.i("MainActivity", t.message ?: "Null message")
            }
        })

         */
        val client = OkHttpClient()
        val request = Request.Builder()
            .url("http://127.0.0.1:8000/")
            .build()
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                Log.i("MainActivity", e.message ?: "Null message")
            }

            override fun onResponse(call: Call, response: Response) {
                val json = response.body?.string() // Get the response body as a JSON string
                Log.i("MainActivity", response.toString())
                response.body?.close() // Close the response body after reading it
            }
        })




    }
}


/*
@Composable
fun MainScreen() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            MainDashboard(navController)
        }
        composable("node_screen/1") {
            Node_page(navController, 1)
        }
        composable("node_screen/2") {
            Node_page(navController, 2)
        }
    }
}

 */
/*
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    SensorAppTheme {
        MainScreen()
    }
}

 */
/*
@Preview(showBackground = true)
@Composable
fun ApiPreview() {
    var testData by remember { mutableStateOf("Loading...") }

    LaunchedEffect(Unit) {
        //val apiService = APIService.getInstance()
        val data = getAPIData( "https://jsonplaceholder.typicode.com/todos/1")//"http://127.0.0.1:5000/dashboard")
        testData = apiService.toString()
    }
    Column {
        Text(text = testData)
    }
}
*/
/*
@Preview(showBackground = true)
@Composable
fun ApiPreview() {
    var headingList by remember { mutableStateOf(emptyList<Heading>()) }


    LaunchedEffect(Unit) {
        headingList = getApiData()
    }

    Column {
        Text(text = "API Response:")
        for (heading in headingList) {
            Text(text = heading.data)
        }
    }
}

 */