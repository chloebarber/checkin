import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
// import { getDeckListing, getDecksByUser } from '../../store/deckListing';
// import './DeckListing.css';


function Checkin_Checkout() {
    // const DeckListing = useSelector((state) => state.DeckListing)
    // const sessionUser = useSelector(state => state.session?.user)
    // const dispatch = useDispatch()


    // useEffect(() => {
    //     if(filter.filter === "ByUser")
    //         dispatch(getDecksByUser(sessionUser.id))
    //     else
    //         dispatch(getDeckListing())
    // }, [dispatch]);

    return (
        <div className="CI_CO_Container">
            <table className = "CI_CO_Table">
            <thead>
                <tr>
                    <th>Room #</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Check In / Check Out</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        </table>
        </div>
    )
}

// {SelectedDeck?.Cards?.map(card => (
//     <tr>
//         <td>{card.card_name}</td>
//         <td>{card.card_text_slot_1}</td>
//         <td>{card.card_text_slot_2}</td>
//         <td>{user.user?.id === SelectedDeck.Deck?.owner_id && ownerOptions("EDITCARD", card)}</td>
//         {/* <td>{<button onClick={(e) => handleEdit(e, card)}>Edit</button>}</td>   */}
//         {/* <td><button>Delete</button></td> */}
//         <td>{user.user?.id === SelectedDeck.Deck?.owner_id && ownerOptions("DELETECARD", card)}</td>    
//     </tr>
// ))}

export default Checkin_Checkout