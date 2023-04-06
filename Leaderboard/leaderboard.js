function LoadRankings(){
    let RankingData = ["Best","Better","Good","Bad","Badder"];
    for(let i=1;i<=RankingData.length;i++){
        console.log("Rank");
        CurrentRank = "Rank"+i;
        Rank = document.getElementById(CurrentRank);
        Rank.appendChild(document.createTextNode(RankingData[i-1]));
    }
}