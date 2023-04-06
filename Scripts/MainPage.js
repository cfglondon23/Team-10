let Listings = [];


function LoadListings(){
  /*
    var AllJobs = {{totalJobs.values()}};
    for(var Job:AllJobs){
        let Date = {{Job.get_date()}};
        let startTime = {{Job.get_startTime()}};
        let endTime = {{Job.get_endTime()}};
        let Location = {{Job.get_location()}};
        let Description = {{job.get_description()}};
        let Name = {{job.get_name()}};
    }

    */




    /*
          <button onclick="buyHire( {{event.get_id()}} )">
            GET JOB!
          </button>
          */
    
  let Name = "Name";
  let Date = "Date";
  let startTime = "Start Time";
  let endTime = "End Time";
  let Location = "Location";
  let Description = "Description";

  ListingsDiv = document.getElementById("Listings");
  Listing = document.createElement("div");
  Listing.className = "card";

  ListingDetails = document.createElement("div");
  ListingDetails.className = "card-details";

  ListingName = document.createElement("h1");
  ListingName.innerText = Name;
  

  ListingDescription = document.createElement("p");
  ListingDescription.className = "text-title";
  ListingDescription.innerText = Description;
  
  ListingLocation = document.createElement("p");
  ListingLocation.innerText = Location;

  ListingDate = document.createElement("p");
  ListingDate.innerText = Date;

  ListingStart = document.createElement("p");
  ListingStart.innerText = startTime;

  ListingEnd = document.createElement("p");
  ListingEnd.innerText = endTime;


  Listing.appendChild(ListingDetails);
  ListingDetails.appendChild(ListingName);
  ListingDetails.appendChild(ListingDescription);
  ListingDetails.appendChild(ListingLocation);
  ListingDetails.appendChild(ListingDate);
  ListingDetails.appendChild(ListingStart);
  ListingDetails.appendChild(ListingEnd);
  ListingsDiv.appendChild(Listing);

  /*
          echo('<div class="card">');
          echo('<div class="card-details">');
          echo('<p class="text-title">'.$row['category_name'].'</p>');
          echo('</div>');          
          echo('<button class="card-button" type="submit" name="categoryID" value="'.$row['ID'].'">');

          echo($row['category_name']);
          echo('</button></div>');


  round_paragraph.innerHTML = "";
  round_text = document.createElement("div");
  round_text.id = "round-text";
  round_text.innerText = "Round: " + round;

  round_paragraph.appendChild(round_text);
    */
}
