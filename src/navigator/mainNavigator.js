import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen010899Navigator from '../features/BlankScreen010899/navigator';
import CopyOfBlankScreen010898Navigator from '../features/CopyOfBlankScreen010898/navigator';
import CopyOfBlankScreen010897Navigator from '../features/CopyOfBlankScreen010897/navigator';
import BlankScreen010894Navigator from '../features/BlankScreen010894/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen010899: { screen: BlankScreen010899Navigator },
CopyOfBlankScreen010898: { screen: CopyOfBlankScreen010898Navigator },
CopyOfBlankScreen010897: { screen: CopyOfBlankScreen010897Navigator },
BlankScreen010894: { screen: BlankScreen010894Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
