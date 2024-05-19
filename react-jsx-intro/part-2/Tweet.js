function Tweet({username, name, date, message}) {
    return (
        <div className="tweet">
            <h3 className="name">{name}</h3>
            <span className="username">@{username}</span>
            <span className="date">{date}</span>
            <p>{message}</p>
        </div>
    )
}