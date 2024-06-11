const trainName_Destination_Map = {
    "train_1": "Chennai",
    "train_2": "Madurai",
    "train_3": "Coimbatore"
}
const getDestination = (trainName) => {
    const destination = trainName_Destination_Map[trainName] ?? "Train Name not found";
    return destination;
} 
export const handler = async (event, context) => {
    
    console.log("Event ", event);
    
    console.log("trainName ", event['queryStringParameters'].trainName);
    const destination =  getDestination(event['queryStringParameters'].trainName);
    console.log("Destination ", destination);
    const response = {
        statusCode: 200,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            place: destination,
            input: event
        })
    };
    
    return response;
};
