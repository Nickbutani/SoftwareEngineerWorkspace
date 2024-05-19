const Max_name_length = 8;

function Person(name, age, hobbies) {
    const voteText = age >= 18 ? "Please go vote!" : "You must be 18.";
    const hobbiesList = hobbies.map(hobby => <li>{hobby}</li>);

    return (
        <div>
            <p>Learn some information about this person:</p>
            <ul>
                <li>{name.length > Max_name_length ? name.slice(0, Max_name_length) : name}</li>
                <li>{age}</li>
                <ul>
                    {hobbiesList}
                </ul>
            </ul>
            <h3>{voteText}</h3>
        </div>
    )
}
