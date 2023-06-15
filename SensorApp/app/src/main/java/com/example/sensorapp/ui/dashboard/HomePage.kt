package com.example.sensorapp.ui.dashboard

import android.annotation.SuppressLint
import android.icu.text.SimpleDateFormat
import android.icu.util.TimeZone
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.Card
import androidx.compose.material.Scaffold
import androidx.compose.material.Text
import androidx.compose.material.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.sensorapp.api.model.Heading
import java.util.*
/*
// Main Dashboard for the Most recent data
@SuppressLint("UnusedMaterialScaffoldPaddingParameter")
@Composable
fun MainDashboard(navController: NavController) {

    val data: Heading() = AppData.heading
    val lastUpdate = getLatestTime(AppData.heading)
    Scaffold(
        topBar = {
            TopAppBar(
                modifier = Modifier.fillMaxWidth(),
                contentPadding = PaddingValues(0.dp)
            ){
                Text(
                    text = "Sensor Live Data",
                    fontSize = 18.sp,
                    textAlign = TextAlign.Center,
                    modifier = Modifier.fillMaxWidth()
                )
            }
        }
    ){
        // Dashboard to view most recent updates from the central hub
        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = formatDate(lastUpdate), //Replace with variable for time unix
                fontSize = 10.sp,
                textAlign = TextAlign.Center)
            Text(
                text = "Last Updated",
                fontSize = 8.sp,
                textAlign = TextAlign.Center)

            Spacer(modifier = Modifier.height(10.dp))

            Column(
                modifier = Modifier.padding(16.dp)
            ){
                // Display the data in a list
                LazyColumn(
                    verticalArrangement = Arrangement.spacedBy(8.dp),
                    contentPadding = PaddingValues(top = 8.dp)
                ) {
                    items(data.size) { index ->
                        val item = data[index]
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { navController.navigate("node_screen/${item.id}") },
                            elevation = 4.dp
                        ) {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.Center,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Box(
                                    Modifier
                                        .align(Alignment.CenterVertically)
                                        .fillMaxWidth()
                                        .height(100.dp)
                                        .background(Color.LightGray)
                                ) {
                                    Text(
                                        text = "Sensor Node #${item.id}",
                                        fontSize = 14.sp,
                                        textAlign = TextAlign.Center,
                                        modifier = Modifier
                                            .padding(vertical = 8.dp)
                                            .align(Alignment.TopCenter)
                                    )
                                    Text(
                                        text = formatDate(item.time),
                                        fontSize = 10.sp,
                                        textAlign = TextAlign.Center,
                                        modifier = Modifier
                                            .padding(bottom = 8.dp)
                                            .align(Alignment.BottomCenter)
                                    )

                                    Column(
                                        modifier = Modifier.align(Alignment.Center),
                                        horizontalAlignment = Alignment.CenterHorizontally
                                    ) {
                                        Row(
                                            modifier = Modifier.fillMaxWidth(),
                                            verticalAlignment = Alignment.CenterVertically,
                                            horizontalArrangement = Arrangement.SpaceEvenly
                                        ) {
                                            Text(
                                                text = "Temperature (°C)",
                                                fontSize = 12.sp,
                                                textAlign = TextAlign.Center
                                            )
                                            Text(
                                                text = "${item.temperature}",
                                                fontSize = 12.sp,
                                                textAlign = TextAlign.Center
                                            )
                                        }
                                        Spacer(modifier = Modifier.height(3.dp))
                                        Row(
                                            modifier = Modifier.fillMaxWidth(),
                                            verticalAlignment = Alignment.CenterVertically,
                                            horizontalArrangement = Arrangement.SpaceEvenly
                                        ) {
                                            Text(
                                                text = "Soil Moisture",
                                                fontSize = 12.sp,
                                                textAlign = TextAlign.Center
                                            )
                                            Text(
                                                text = "${item.soilMoisture}",
                                                fontSize = 12.sp,
                                                textAlign = TextAlign.Center
                                            )
                                        }
                                    }
                                    Spacer(
                                        modifier = Modifier
                                            .height(8.dp)
                                            .align(Alignment.BottomCenter)
                                    )
                                    Text(
                                        text = "View More...",
                                        color = Color.Blue,
                                        fontSize = 9.sp,
                                        textAlign = TextAlign.Center,
                                        modifier = Modifier
                                            .align(Alignment.BottomEnd)
                                            .padding(end = 16.dp, bottom = 8.dp)
                                    )
                                }
                            }
                        }
                    }
                }
            }

            Spacer(modifier = Modifier.height(26.dp))

            // Tips and Suggestions Section of the code
            Column (
                modifier = Modifier.fillMaxWidth(),
                verticalArrangement = Arrangement.SpaceBetween,
                horizontalAlignment = Alignment.CenterHorizontally
            ){
                Text(
                    text = "Alerts and Suggestions",
                    color = Color.Red,
                    fontSize = 18.sp,
                    textAlign = TextAlign.Center,
                    textDecoration = TextDecoration.Underline
                )
                Column(
                    modifier = Modifier.fillMaxWidth(),
                    verticalArrangement = Arrangement.SpaceBetween
                ) {
                    Spacer(modifier = Modifier
                        .height(10.dp)
                        .fillMaxWidth() )

                    Text(
                        text ="First Tip/Suggestion",
                        fontSize = 15.sp,
                        textAlign = TextAlign.Left
                    )
                    Text(
                        text ="Second Tip/Suggestion",
                        fontSize = 15.sp,
                        textAlign = TextAlign.Left
                    )
                    Text(
                        text ="Third Tip/Suggestion",
                        fontSize = 15.sp,
                        textAlign = TextAlign.Left
                    )
                }
            }

        }


    }
}

@SuppressLint("SimpleDateFormat")
fun formatDate(unixTime: Long): String {
    val sdf = SimpleDateFormat("dd:MM:yyyy HH:mm")
    sdf.timeZone = TimeZone.getTimeZone("EST")
    return sdf.format(Date(unixTime * 1000))
}

fun getLatestTime(headings: List<Heading>): Long {
    var latestTime: Long? = null
    for (heading in headings) {
        if (latestTime == null || heading.time > latestTime) {
            latestTime = heading.time
        }
    }
    return latestTime ?: 0L
}


 */