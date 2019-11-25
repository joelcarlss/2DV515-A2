import React, { useEffect, useState } from 'react'
import { getCluster } from '../model/api'
import { makeStyles } from '@material-ui/core/styles'
import TreeView from '@material-ui/lab/TreeView'
import ExpandMoreIcon from '@material-ui/icons/ExpandMore'
import ChevronRightIcon from '@material-ui/icons/ChevronRight'
import TreeItem from '@material-ui/lab/TreeItem'

const useStyles = makeStyles({
  root: {
    height: 216,
    flexGrow: 1,
    maxWidth: 400
  }
})

export default function Tree () {
  const classes = useStyles()
  const [cluster, setCluster] = useState()

  useEffect(() => {
    setCluster(getCluster())
  }, [])

  const renderTreeChilds = () => {
    if (cluster !== undefined) {
      return <div>

        {cluster.map((arr, y) => (

          <TreeItem nodeId={y} label={`${'cluster ' + y}`}>

            {arr.map((x, i) => (

              <TreeItem nodeId={(i + y + 1)} label={x} />

            ))}
          </TreeItem>
        ))}
      </div>
    }
  }
  return (
    <TreeView
      className={classes.root}
      defaultCollapseIcon={<ExpandMoreIcon />}
      defaultExpandIcon={<ChevronRightIcon />}
    >
      {renderTreeChilds()}
    </TreeView>
  )
}
