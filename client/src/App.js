import React from 'react'
import Tree from './components/Tree'
// import Table from './components/DenseTable'
// import SimpleSelect from './components/SimpleSelect'
import { Provider } from './useAppState'
import List from '@material-ui/core/List'
import './App.css'
import CssBaseline from '@material-ui/core/CssBaseline'
import Container from '@material-ui/core/Container'

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <div>
          <CssBaseline />
          <Container maxWidth='sm'>
            <List style={{ maxHeight: '100%', overflow: 'visible' }} >
              <Tree />
            </List>
          </Container>
        </div>
      </header>
    </div>
  )
}

export default () => <Provider><App /></Provider>
