//
//  Onyo_challengeUITests.swift
//  Onyo-challengeUITests
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import XCTest

class Onyo_challengeUITests: XCTestCase {
        
    override func setUp() {
        super.setUp()
        
        continueAfterFailure = false
        XCUIApplication().launch()
    }
    
    func testMainFlow() {
        let app = XCUIApplication()
        
        XCUIApplication().navigationBars["Onyo_challenge.CompanyView"].buttons["onyo"].tap()
        sleep(3)
        XCUIDevice.sharedDevice().orientation = .Portrait
        XCTAssertTrue(app.tables.cells.count > 0, "Companies not loaded or timeout occured")
        app.tables.cells.elementBoundByIndex(0).tap()
        XCTAssertTrue(app.collectionViews.cells.count > 0, "Categories not loaded or timeout occured")
        
        let tabBarsQuery = app.tabBars
        app.navigationBars["Onyo_challenge.OnyoTabBar"].buttons["onyo"].tap()
        tabBarsQuery.buttons["Home"].tap()
        tabBarsQuery.buttons["Resgate"].tap()
        tabBarsQuery.buttons["Cardápio"].tap()
        app.navigationBars["Onyo_challenge.OnyoTabBar"].buttons[" "].tap()
    }
    
}
