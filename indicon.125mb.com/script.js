var urlTxt="https://iotdatos.firebaseio.com/.json";
var jsonFile = new XMLHttpRequest();
jsonFile.open("GET",urlTxt,false);
jsonFile.send();
var data = JSON.parse(jsonFile.response);
var ejeX = data.MyTestData.Registrodatosx.ejex;
var ejeY = data.MyTestData.Registrodatosy.ejey;
var ejeZ = data.MyTestData.Registrodatosz.ejez;
var tiempo_eje = data.MyTestData.html.Arreglo_tiempo;
var total_veces_alto_x = data.MyTestData.Reg_pel_xa;
var total_veces_medio_x = data.MyTestData.Reg_pel_xm;
var total_veces_alto_y = data.MyTestData.Reg_pel_ya;
var total_veces_medio_y = data.MyTestData.Reg_pel_ym;
var total_veces_alto_z = data.MyTestData.Reg_pel_za;
var total_veces_medio_z = data.MyTestData.Reg_pel_zm;
var ejeX_min = data.MyTestData.Reg_x4.ejex;
var ejeY_min = data.MyTestData.Reg_y4.ejey;
var ejeZ_min = data.MyTestData.Reg_z4.ejez;
var tiempo_transcurrido = data.MyTestData.tiempo.transcurrido;

var porcentaje_x_medio = (total_veces_medio_x/172)*100;
var porcentaje_x_alto = (total_veces_alto_x/172)*100;
var porcentaje_diferenciax = 100-(porcentaje_x_medio)-(porcentaje_x_alto);
var total_porx = porcentaje_x_medio + porcentaje_x_alto;


var porcentaje_y_alto = (total_veces_alto_y/172)*100;
var porcentaje_y_medio = (total_veces_medio_y/172)*100;
var porcentaje_diferenciay = 100-(porcentaje_y_alto)-(porcentaje_y_medio);
var total_pory = porcentaje_y_alto + porcentaje_y_medio;


var porcentaje_z_alto = (total_veces_alto_z/172)*100;
var porcentaje_z_medio = (total_veces_medio_z/172)*100;
var porcentaje_diferenciaz = 100-(porcentaje_z_alto)-(porcentaje_z_medio);
var total_porz = porcentaje_z_alto+ porcentaje_z_medio;

var colors = ['#007bff','#28a745','#333333','#c3e6cb','#dc3545','#6c757d'];

var nuev_temp = (tiempo_transcurrido)/0.35


var arret =  new Array(172);
for(var i = 0; i <= 171; i++){
  arret[i]= Math.round(0.35*i);
  i += 1;
}

var referencia_media = new Array(172);
for(var i = 0; i <= 171; i++){
  referencia_media[i]=0.09;
  i += 1;
}

var referencia_alta = new Array(172);
for(var i = 0; i <= 171; i++){
  referencia_alta[i]=0.15;
  i += 1;
}
var nuevo_final_tiempo = new Array(nuev_temp);
for(var i = 0; i <=(nuev_temp) ;  i++){
  nuevo_final_tiempo[i] =Math.round(0.35*i);
  i += 1;
}

var referencia_media_tra_completa = new Array(nuev_temp);
for(var i = 0; i <= nuev_temp; i++){
  referencia_media_tra_completa [i]= 0.09;
  i += 1;
}

var referencia_alta_tra_completa = new Array(nuev_temp);
for(var i = 0; i <= nuev_temp; i++){
   referencia_alta_tra_completa[i]= 0.15;
  i += 1;
}

/*condicional para la clasificacion de x medio */
if(porcentaje_x_medio < 9.48 ){
  var cla_buenox = 'Bueno';
  document.getElementById('resul_x_medio_buen').innerHTML = cla_buenox ;
}

if( 9.48 < porcentaje_x_medio &&  porcentaje_x_medio < 13.5 ){
  var cla_regx = 'regular';
  document.getElementById('resul_x_medio_reg').innerHTML = cla_regx ;
}
if(porcentaje_x_medio > 13.5 ){
  var cla_malx = 'malo';
  document.getElementById('resul_x_medio_mal').innerHTML = cla_malx ;
}

/*condicional para la clasificacion de x alto */
if(porcentaje_x_alto < 2.94 ){
  var cla_buenox_a = 'Bueno';
  document.getElementById('resul_x_alto_buen').innerHTML = cla_buenox_a ;
}
if(2.94 < porcentaje_x_alto && porcentaje_x_alto < 4.28 ){
  var cla_regx_a = 'Regular';
  document.getElementById('resul_x_alto_reg').innerHTML = cla_regx_a ;
}
if(porcentaje_x_alto > 4.28 ){
  var cla_malx_a = 'Malo';
  document.getElementById('resul_x_alto_mal').innerHTML = cla_malx_a ;
}

/*condicional para la clasificacion de y medio */
if(porcentaje_y_medio < 14.69 ){
  var cla_buenoy = 'Bueno';
  document.getElementById('resul_y_medio_buen').innerHTML = cla_buenoy ;
}
if(14.69 < porcentaje_y_medio &&  porcentaje_y_medio < 16.52){
  var cla_regy = 'Regular';
  document.getElementById('resul_y_medio_reg').innerHTML = cla_regy ;
}
if(porcentaje_y_medio > 16.52 ){
  var cla_maly = 'Malo';
  document.getElementById('resul_y_medio_mal').innerHTML = cla_maly ;
}

/*condicional para la clasificacion de y alto */
if(porcentaje_y_alto < 5.3 ){
  var cla_buenoy_a = 'Bueno';
  document.getElementById('resul_y_alto_buen').innerHTML = cla_buenoy_a ;
}
if( 5.3 < porcentaje_y_alto &&  porcentaje_y_alto < 6.73  ){
  var cla_regy_a = 'Regular';
  document.getElementById('resul_y_alto_reg').innerHTML = cla_regy_a ;
}
if(porcentaje_y_alto > 6.73 ){
  var cla_maly_a = 'Malo';
  document.getElementById('resul_y_alto_mal').innerHTML = cla_maly_a ;
}

/*condicional para la clasificacion de z medio */
if(porcentaje_z_medio < 20.17 ){
  var cla_buenoz = 'Bueno';
  document.getElementById('resul_z_medio_buen').innerHTML = cla_buenoz ;
}
if( 20.17 < porcentaje_z_medio &&  porcentaje_z_medio < 23.31){
  var cla_regz = 'Regular';
  document.getElementById('resul_z_medio_reg').innerHTML = cla_regz ;
}
if(porcentaje_z_medio > 23.31 ){
  var cla_malz = 'Malo';
  document.getElementById('resul_z_medio_mal').innerHTML = cla_malz ;
}

/*condicional para la clasificacion de z alto */
if( porcentaje_z_alto < 6.8 ){
  var cla_buenoz_a = 'Bueno';
  document.getElementById('resul_z_alto_buen').innerHTML = cla_buenoz_a ;
}
if( 6.8 < porcentaje_z_alto &&  porcentaje_z_alto < 9.88 ){
  var cla_regz_a = 'Regular';
  document.getElementById('resul_z_alto_reg').innerHTML = cla_regz_a ;
}
if( porcentaje_z_alto > 9.88 ){
  var cla_malz_a = 'Malo';
  document.getElementById('resul_z_alto_mal').innerHTML =cla_malz_a ;
}
/* Condicional clasificacion x total */
if( total_porx < 12.75 ){
  var cla_total_x_buen = 'Bueno';
  document.getElementById('cla_total_x_bue').innerHTML = cla_total_x_buen ;
}
if(12.75 < total_porx  && total_porx < 16.31 ){
  var cla_total_x_reg = 'Regular';
  document.getElementById('cla_total_x_re').innerHTML = cla_total_x_reg ;
}
if( total_porx > 16.31 ){
  var cla_total_x_mal = 'Malo';
  document.getElementById('cla_total_x_ma').innerHTML = cla_total_x_mal ;
}


/* Condicional clasificacion y total */
if( total_pory < 20.11 ){
  var cla_total_y_buen = 'Bueno';
  document.getElementById('cla_total_y_bue').innerHTML = cla_total_y_buen ;
}
if( 20.11 < total_pory  && total_pory < 23.56){
  var cla_total_y_reg = 'Regular';
  document.getElementById('cla_total_y_re').innerHTML = cla_total_y_reg;
}
if( total_pory > 23.56){
  var cla_total_y_mal = 'Malo';
  document.getElementById('cla_total_y_ma').innerHTML = cla_total_y_mal ;
}

/* Condicional clasificacion z total */
if( total_porz < 26.99){
  var cla_total_z_buen = 'Bueno';
  document.getElementById('cla_total_z_bue').innerHTML = cla_total_z_buen ;
}
if(  26.99 < total_porz  && total_porz < 33.66 ){
  var cla_total_z_reg = 'Regular';
  document.getElementById('cla_total_z_re').innerHTML = cla_total_z_reg ;
}
if( total_porz > 33.66){
  var cla_total_z_mal = 'Malo';
  document.getElementById('cla_total_z_ma').innerHTML = cla_total_z_mal;
}



/* large line chart */
var chLine = document.getElementById("chLine");
var chartData = {
  labels: arret,
  datasets: [{
    data: ejeX_min,
    label: 'ejex',
    backgroundColor: 'transparent',
    borderColor: colors[0],
    borderWidth: 0.5,
    pointBackgroundColor: colors[0]
  },
 {
     data: ejeY_min,
     label: 'ejey',
   backgroundColor: 'transparent',
    borderColor: colors[1],
    borderWidth: 0.5,
    pointBackgroundColor: colors[1]
  },
  {
      data: referencia_media,
      label: 'Referencia riesgo medio',
    backgroundColor: 'transparent',
     borderColor: 'orange',
     borderWidth: 0.5,
     pointBackgroundColor: 'orange'
   },
   {
       data: referencia_alta,
       label: 'Referencia riesgo alto',
     backgroundColor: 'transparent',
      borderColor: colors[3],
      borderWidth: 0.5,
      pointBackgroundColor: colors[3]
    },
  {
      data: ejeZ_min,
      label: 'ejez',
    backgroundColor: 'transparent',
     borderColor: colors[4],
     borderWidth: 0.5,
     pointBackgroundColor: colors[4]
   }
  ]
};
if (chLine) {
  new Chart(chLine, {
  type: 'line',
  data: chartData,
  options: {
    title: {
      display: true,
      text: 'Acelerometro Correspondinete a 1 min'
    },
    scales: {
      xAxes: [{
        ticks: {
          beginAtZero: false,
          precision:0,
          autoSkip: true,
          maxTicksLimit: 24
        }
      }]
    },
    legend: {
      display: true
    },
    responsive: true
  }
  });
}
/* large pie/donut chart */

/* bar chart */
var chBar = document.getElementById("chBar");
if (chBar) {
  new Chart(chBar, {
  type: 'bar',
  data: {
    labels: ["ejex", "ejey", "ejez"],
    datasets: [{
      data: [porcentaje_x_medio,porcentaje_y_medio,porcentaje_z_medio],
      label: 'riesgo medio',
      backgroundColor: colors[0]
    },
    {
      data: [porcentaje_x_alto,porcentaje_y_alto,porcentaje_z_alto],
      label: 'riesgo alto',
      backgroundColor: colors[1]
    }
  ]
  },
  options: {
    legend: {
      display: true
    },
    title: {
      display: true,
      text: 'Porcentaje incidencia de Riesgo por eje'
    },
    scales: {
      xAxes: [{
        barPercentage: 0.4,
        categoryPercentage: 0.5
      }]
    }
  }
  });
}

/* 3 donut charts */
var donutOptions = {
  cutoutPercentage: 50,
  title: {
    display: true,
    text: 'Porcentaje de Riesgo'
  },
  legend: {position:'bottom', padding:5, labels: {pointStyle:'circle', usePointStyle:false}}
};

// donut 1
var chDonutData1 = {
    labels: ['%alto eje x', '%medio eje x', '% bueno eje x'],
    datasets: [
      {
        backgroundColor: colors.slice(0,3),
        borderWidth: 0,
        data: [porcentaje_x_alto, porcentaje_x_medio, porcentaje_diferenciax]
      }
    ]
};

var chDonut1 = document.getElementById("chDonut1");
if (chDonut1) {
  new Chart(chDonut1, {
      type: 'pie',
      data: chDonutData1,
      options: donutOptions
  });
}

// donut 2
var chDonutData2 = {
    labels: [' %alto eje y', '%medio eje y', '%bueno eje y'],
    datasets: [
      {
        backgroundColor: colors.slice(0,3),
        borderWidth: 0,
        data: [porcentaje_y_alto, porcentaje_y_medio, porcentaje_diferenciay]
      }
    ]
};
var chDonut2 = document.getElementById("chDonut2");
if (chDonut2) {
  new Chart(chDonut2, {
      type: 'pie',
      data: chDonutData2,
      options: donutOptions
  });
}

// donut 3
var chDonutData3 = {
    labels: ['%alto eje z', ' %medio eje z', '%bueno eje z'],
    datasets: [
      {
        backgroundColor: colors.slice(0,3),
        borderWidth: 0,
        data: [porcentaje_z_alto, porcentaje_z_medio,porcentaje_diferenciaz]
      }
    ]
};
var chDonut3 = document.getElementById("chDonut3");
if (chDonut3) {
  new Chart(chDonut3, {
      type: 'pie',
      data: chDonutData3,
      options: donutOptions
  });
}


var completo = document.getElementById("completo");
var chartData = {
  labels: nuevo_final_tiempo,
  datasets: [{
    data: ejeX,
    label: 'ejex',
    backgroundColor: 'transparent',
    borderColor: colors[0],
    borderWidth: 0.5,
    pointBackgroundColor: colors[0]
  },
  {
      data: referencia_media_tra_completa,
      label: 'Referencia riesgo medio',
    backgroundColor: 'transparent',
     borderColor: 'orange',
     borderWidth: 0.5,
     pointBackgroundColor: 'orange'
   },
   {
       data: referencia_alta_tra_completa,
       label: 'Referencia riesgo alto',
     backgroundColor: 'transparent',
      borderColor: 'Purple',
      borderWidth: 0.5,
      pointBackgroundColor: 'Purple'
    },

 {
     data: ejeY,
     label: 'ejey',
   backgroundColor: 'transparent',
    borderColor: colors[1],
    borderWidth: 0.5,
    pointBackgroundColor: colors[1]
  },
  {
      data: ejeZ,
      label: 'ejez',
    backgroundColor: 'transparent',
     borderColor: colors[4],
     borderWidth: 0.5,
     pointBackgroundColor: colors[4]
   }
  ]
};
if (completo) {
  new Chart(completo, {
  type: 'line',
  data: chartData,
  options: {
    title: {
      display: true,
      text: 'Acelerometro Correspondinete al Trayecto'
    },
    scales: {
      xAxes: [{
        ticks: {
          beginAtZero: false,
          precision:0,
          autoSkip: true,
          maxTicksLimit: 24
        }
      }]
    },
    legend: {
      display: true
    },
    responsive: true
  }
  });
}
