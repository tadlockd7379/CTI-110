const giannisID = 15;
const currentSeason = 2022;

async function fetchStats(id = giannisID, season = currentSeason) {
    const req = await fetch(`https://www.balldontlie.io/api/v1/stats?player_ids[]=${id}&seasons[]=${season}`);
    return await req.json();
}

async function main() {
    const giannis = (await fetchStats()).data;
    console.log(giannis);

    giannis.forEach(game => {
        let start = '<tr>';
        let date = '<td>' + new Date(game.game.date).toISOString().replace('-', '/').split('T')[0].replace('-', '/') + '</td>';
        let points = '<td>' + game.pts + '</td>';
        let assists = '<td>' + game.ast + '</td></tr>';

        document.getElementById('stats').innerHTML += start + date + points + assists;
    });
}

main();