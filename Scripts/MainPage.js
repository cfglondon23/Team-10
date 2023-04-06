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
  
  dummy_jobs = [
    {
                "id": 1,
                "name": "Charity Run",
                "location": "Central Park",
                "description": "Help us organize a charity run in Central Park.",
                "date": "28th",
                "startTime": "9am",
                "endTime": "10pm"
    },
    {
                "id": 2,
                "name": "Food Drive",
                "location": "New York City Food Bank",
                "description": "We need volunteers to help distribute food to families in need.",
                "date": "28th",
                "startTime": "9am",
                "endTime": "10pm"
    },
    {
                "id": 3,
                "name": "Beach Cleanup",
                "location": "Rockaway Beach",
                "description": "Help us keep our beaches clean!",
                "date": "28th",
                "startTime": "9am",
                "endTime": "10pm"
    }
  ]
         
  for(var i=0;i<=dummy_jobs.length;i++){
    let dummy_job = dummy_jobs[i];

    let Name = dummy_job["name"];
    let Date = "Date: "+dummy_job["date"];
    let startTime = "Start Time: "+dummy_job["startTime"];
    let endTime = "End Time: "+dummy_job["endTime"];
    let Location = "Location: "+dummy_job["location"];
    let Description = "Description: "+dummy_job["description"];

    ListingsDiv = document.getElementById("Listings");
    Listing = document.createElement("div");
    Listing.className = "card";

    ListingDetails = document.createElement("div");
    ListingDetails.className = "card-details";

    ListingName = document.createElement("h1");
    ListingName.innerText = Name;
    ListingName.className = "text";
  
    ListingDescription = document.createElement("p");
    ListingDescription.className = "text-title";
    ListingDescription.innerText = Description;
    ListingDescription.className = "text";
    
    ListingLocation = document.createElement("p");
    ListingLocation.innerText = Location;
    ListingLocation.className = "text";

    ListingDate = document.createElement("p");
    ListingDate.innerText = Date;
    ListingDate.className = "text";

    ListingStart = document.createElement("p");
    ListingStart.innerText = startTime;
    ListingStart.className = "text";

    ListingEnd = document.createElement("p");
    ListingEnd.innerText = endTime;
    ListingEnd.className = "text";
  

    ListingButton = document.createElement("button");
    ListingButton.className = "card-button";
    ListingButton.innerText = "Get Job";
    ListingButton.setAttribute("onclick","RedirectPage()")


    Listing.appendChild(ListingDetails);
    ListingDetails.appendChild(ListingName);
    
    ListingDetails.appendChild(ListingDescription);
    ListingDetails.appendChild(ListingLocation);
    ListingDetails.appendChild(ListingDate);
    ListingDetails.appendChild(ListingStart);
    ListingDetails.appendChild(ListingEnd);
    
    ListingDetails.appendChild(ListingButton);
    ListingsDiv.appendChild(Listing);
  }
}

function RedirectPage(){
  location.href="job.html";
}