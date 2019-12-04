import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import PersonPinIcon from '@material-ui/icons/PersonPin';
import StorefrontIcon from '@material-ui/icons/Storefront';
import RestoreIcon from '@material-ui/icons/Restore';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Nav from './Nav';
import Login from './Login';


function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`scrollable-prevent-tabpanel-${index}`}
      aria-labelledby={`scrollable-prevent-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `scrollable-prevent-tab-${index}`,
    'aria-controls': `scrollable-prevent-tabpanel-${index}`,
  };
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    width: '100%',
    backgroundColor: theme.palette.background.paper,
  },
}));

export default function ScrollableTabsButtonPrevent() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Tabs
          value={value}
          onChange={handleChange}
          variant="scrollable"
          scrollButtons="off"
          aria-label="scrollable prevent tabs example"
        >
          <Tab icon={<ExitToAppIcon />} aria-label="person" {...a11yProps(0)} />
          <Tab icon={<PersonPinIcon />} aria-label="phone" {...a11yProps(1)} />
          <Tab icon={<StorefrontIcon />} aria-label="favorite" {...a11yProps(2)} />
          <Tab icon={<RestoreIcon />} aria-label="person" {...a11yProps(3)} />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <Login>
          
        </Login>
      </TabPanel>
      <TabPanel value={value} index={1}>
        Item One
      </TabPanel>
      <TabPanel value={value} index={2}>
        <Nav>

        </Nav>
      </TabPanel>
      <TabPanel value={value} index={3}>
        Item Three
      </TabPanel>
    </div>
  );
}