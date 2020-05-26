/**
 * Created by kosty on 26.05.2020.
 */
Highcharts.theme = {
  colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572',
    '#FF9655', '#FFF263', '#6AF9C4'],
  chart: {
    backgroundColor: {
        color: '#000'
    },
  },
  title: {
    style: {
      color: '#fff',
      font: 'bold 20px "Trebuchet MS", Verdana, sans-serif'
    }
  },
  subtitle: {
    style: {
      color: '#666666',
      font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
    }
  },
  legend: {
    itemStyle: {
      font: '9pt Trebuchet MS, Verdana, sans-serif',
      color: '#fff'
    },
    itemHoverStyle: {
      color: 'gray'
    }
  }
};

// Apply the theme
Highcharts.setOptions(Highcharts.theme);