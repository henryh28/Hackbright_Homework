// PART 1: SHOW A FORTUNE
async function showFortune() {
  const response = await fetch("/fortune");
  const fortune = await response.text();
  document.querySelector("#fortune-text").innerHTML = fortune;
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);


// PART 2: SHOW WEATHER
async function showWeather(evt) {
  evt.preventDefault();
  const zipcode = document.querySelector('#zipcode-field').value;
  const url = `/weather?zipcode=${zipcode}`;

  const response = await fetch(url);
  const forecast = await response.json();
  document.getElementById("weather-info").innerHTML = forecast.forecast;
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);
