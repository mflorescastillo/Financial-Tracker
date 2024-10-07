import React, { useState } from 'react';

const CarPriceForm = () => {
    const [make, setMake] = useState('');
    const [model, setModel] = useState('');
    const [price, setPrice] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: JSON.stringify({ make, model, price }),
            headers: { 'Content-Type': 'application/json' }
        });
        if (response.ok) {
            alert("Car price added!");
        } else {
            alert("Failed to add car price.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={make} onChange={(e) => setMake(e.target.value)} placeholder="Make" required />
            <input type="text" value={model} onChange={(e) => setModel(e.target.value)} placeholder="Model" required />
            <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" required />
            <button type="submit">Add Car Price</button>
        </form>
    );
};

export default CarPriceForm;