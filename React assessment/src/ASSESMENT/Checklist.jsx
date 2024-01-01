import React, { useState, useContext } from 'react';

// Create a context to manage the state globally
const ChecklistContext = React.createContext();

// Checklist component
const Checklist = () => {
  // Step 1: Create React state to track checkbox value
  const [citizenChecked, setCitizenChecked] = useState(false);
  const [over21Checked, setOver21Checked] = useState(false);

  // Step 2: Function to update checkbox value based on event.target.checked
  const handleCheckboxChange = (checkboxType) => {
    if (checkboxType === 'citizen') {
      setCitizenChecked((prevCitizenChecked) => !prevCitizenChecked);
    } else if (checkboxType === 'over21') {
      setOver21Checked((prevOver21Checked) => !prevOver21Checked);
    }
  };

  // Step 4: Implement useContext Hooks for this task
  const contextValue = {
    citizenChecked,
    over21Checked,
    handleCheckboxChange,
  };

  return (
    // Step 3: Add checkbox input element to JSX code with onChange function
    <ChecklistContext.Provider value={contextValue}>
      <div>
        <h2>Checklist</h2>
        {/* Display selected options dynamically */}
        <h1>Are you a Citizen: {citizenChecked ? 'Yes' : 'No'}</h1>
        <h1>Are you over 21: {over21Checked ? 'Yes' : 'No'}</h1>
        {/* Options with checkboxes */}
        <label>
          <input
            type="checkbox"
            checked={citizenChecked}
            onChange={() => handleCheckboxChange('citizen')}
          />
          Are you a Citizen?
        </label>

        <br />

        <label>
          <input
            type="checkbox"
            checked={over21Checked}
            onChange={() => handleCheckboxChange('over21')}
          />
          Are you over 21?
        </label>
      </div>
    </ChecklistContext.Provider>
  );
};

// Component to consume the ChecklistContext
const DisplaySelectedOptions = () => {
  const { citizenChecked, over21Checked } = useContext(ChecklistContext);

  return (
    <div>
      <h3>Display Selected Options</h3>
      <p>Are you a Citizen: {citizenChecked ? 'Yes' : 'No'}</p>
      <p>Are you over 21: {over21Checked ? 'Yes' : 'No'}</p>
    </div>
  );
};

// Example usage
// const App = () => {
//   return (
//     <div>
//       <Checklist />
//       <DisplaySelectedOptions />
//     </div>
//   );
// };

export default Checklist;

