package com.example.sensorapp.ui.dashboard

import android.annotation.SuppressLint
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController

@SuppressLint("UnusedMaterialScaffoldPaddingParameter")
@Composable
fun Node_page(navController: NavController, nodeId: Int){
    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        "Sensor Live Data",
                        modifier = Modifier.fillMaxWidth(),
                        textAlign = TextAlign.Center) },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back") }
                }
            )
        }
    ){
        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.CenterHorizontally
        ){
            Text(
                text = "Time of Update", //Replace with variable for time unix
                fontSize = 10.sp,
                textAlign = TextAlign.Center)
            Text(
                text = "Last Updated",
                fontSize = 8.sp,
                textAlign = TextAlign.Center)

            Spacer(modifier = Modifier.height(10.dp))

            Column(
                modifier = Modifier.fillMaxWidth(),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                //DataList(nodeId)
            }

            Spacer(modifier = Modifier.height(10.dp))
        }
    }
}
/*
@Composable
fun DataList(nodeId: Int) {
    val data: List<Data> = if (nodeId == 1) {
        AppData.data1
    } else {
        AppData.data2
    }

    Column(
        modifier = Modifier.padding(16.dp)
    ) {
        // Display the data in a list
        LazyColumn(
            verticalArrangement = Arrangement.spacedBy(8.dp),
            contentPadding = PaddingValues(top = 8.dp)
        ) {
            items(data.size) { index ->
                val item = data[index]
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    elevation = 4.dp
                ) {
                    Column(
                        modifier = Modifier.padding(8.dp)
                    ) {
                        Text(text = "Time: ${formatDate(item.time)}")
                        Text(text = "Temperature: ${item.temperature} °C")
                        Text(text = "Soil Moisture: ${item.soilMoisture}")
                    }
                }
            }
        }
    }
}

 */
