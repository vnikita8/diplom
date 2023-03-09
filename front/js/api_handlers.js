let favorite_list = fetch('http://127.0.0.1:8000/get_favorite_list/', { 
    method: 'GET',
    mode: 'cors',
  }).then(function(response) { return response.json(); })          
  .then((jsonData)=> {return jsonData;})


const printFavorites = () => {
    favorites.then((a) => {
      console.log(a);
    });
  };

  