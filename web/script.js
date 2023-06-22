function createInsertStatements(data) {
  const insertStatements = [];

  function processObject(tableName, records) {
    const keys = [];
    const values = [];

    for (const key in records) {
      if (records.hasOwnProperty(key)) {
        const value = records[key];

        if (typeof value === 'object') {
          if (Array.isArray(value)) {
            processArray(tableName, value); // Recursively process nested arrays
          } else if(value == null) {
            continue;
          } else {
            processObject(key, value)
          }
          continue; // Skip nested objects
        }

        keys.push(key);

        if (typeof value === 'string') {
          values.push(`'${value}'`);
        } else {
          values.push(String(value));
        }
      }
    }

    const insertStatement = `INSERT INTO ${tableName} ([${keys.join('], [')}]) VALUES (${values.join(', ')});`;
    insertStatements.push(insertStatement);
  }

  function processArray(tableName, records) {
    for (const record of records) {
      if (typeof record === 'object') {
        processObject(tableName, record); // Recursively process objects within the array
      }
    }
  }

  for (const tableName in data) {
    if (data.hasOwnProperty(tableName)) {
      const records = data[tableName];
      
      if (typeof records === 'object') {
        if (Array.isArray(records)) {
          processArray(tableName, records);
        } else {
          processObject(tableName, records);
        }
      }
    }
  }

  return insertStatements;
}

function convertJSONToSQL() {
  const jsonInput = document.getElementById('jsonInput');
  const sqlOutput = document.getElementById('sqlOutput');

  try {
    const json = JSON.parse(jsonInput.value);
    const insertStatements = createInsertStatements(json);
    sqlOutput.textContent = insertStatements.join('\n');
    if (insertStatements.length > 0) {
        copyBtn.disabled = false; // Enable the copy button if there is SQL output
    }
  } catch (error) {
    sqlOutput.textContent = 'Invalid JSON';
  }

  
}

function copyToClipboard() {
    const sqlOutput = document.getElementById('sqlOutput');
    const range = document.createRange();
    range.selectNode(sqlOutput);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
  }
  

const convertBtn = document.getElementById('convertBtn');
convertBtn.addEventListener('click', convertJSONToSQL);

const copyBtn = document.getElementById('copyBtn');
copyBtn.addEventListener('click', copyToClipboard);
