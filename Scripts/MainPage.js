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
  for(var i=0;i<5;i++){

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
    ListingName.className = "text";
    
    ListingDetails.appendChild(document.createTextNode(Description));
    ListingDetails.appendChild(document.createTextNode("<br>"));
    ListingDetails.appendChild(document.createTextNode(Location));
    ListingDetails.appendChild(document.createTextNode(Date));
    ListingDetails.appendChild(document.createTextNode(startTime));
    ListingDetails.appendChild(document.createTextNode(endTime));

  /*
    ListingDescription = document.createElement("p");
    ListingDescription.className = "text-title";
    ListingDescription.innerText = Description;
    ListingDescription.className = "text";
    
    ListingLocation = document.createElement("p");
    ListingLocation.innerText = Location;
    ListingLocation.className = "text";

    ListingDate = document.createElement("p");
    ListingDate.innerText = Date;

    ListingStart = document.createElement("p");
    ListingStart.innerText = startTime;

    ListingEnd = document.createElement("p");
    ListingEnd.innerText = endTime;
    */

    ListingButton = document.createElement("button");
    ListingButton.className = "card-button";
    ListingButton.innerText = "Get Job";
    ListingButton.setAttribute("onclick","RedirectPage()")


    Listing.appendChild(ListingDetails);
    ListingDetails.appendChild(ListingName);
    /*
    ListingDetails.appendChild(ListingDescription);
    ListingDetails.appendChild(ListingLocation);
    ListingDetails.appendChild(ListingDate);
    ListingDetails.appendChild(ListingStart);
    ListingDetails.appendChild(ListingEnd);
    */
    ListingDetails.appendChild(ListingButton);
    ListingsDiv.appendChild(Listing);
  }
}

function RedirectPage(){
  location.href="DescriptionPage.html";
}