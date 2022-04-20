async function submitProfile(evt) {
  evt.preventDefault();

  const data = {
    name: document.querySelector('#name-field').value,
    age: document.querySelector('#age-field').value,
    occupation: document.querySelector('#occupation-field').value
  };

  const response = await fetch("/api/profile", {method: "POST", body: JSON.stringify(data), headers: {'Content-Type': 'application/json'}})
  const profileData = await response.json() 
  
  document.querySelector("#profiles").insertAdjacentHTML("beforeend", `<p>Name: ${profileData.fullname} - 
    Age: ${profileData.age} - Occupation: ${profileData.job}</p>`)
}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
