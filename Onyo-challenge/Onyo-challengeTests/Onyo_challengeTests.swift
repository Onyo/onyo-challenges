//
//  Onyo_challengeTests.swift
//  Onyo-challengeTests
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import XCTest
import Alamofire
import RealmSwift

@testable import Onyo_challenge

class Onyo_challengeTests: XCTestCase {
    
    let validCompanyDict: [String: AnyObject] = ["numericalId":34, "address": "Av. Dr. Chucri Zaidan, 902 Vila Cordeiro - São Paulo, SP - 04583-110", "displayName": "Shopping Marketplace", "geoLat": "-23.6208885000", "geoLon": "-46.6997586000", "image": [["context": "company-main", "height":894, "url": "http://images.onyo.com/JqgeR-gdLKqa-jydKhFN7DihYTg=/0x0:1600x894/fit-in/912x510/https://onyo.s3.amazonaws.com/picture/0d1516c3cd0a4dbcb3c65c92db97aa0f.jpg", "width":1600], ["context": "company-main", "height":894, "url": "http://images.onyo.com/JqgeR-gdLKqa-jydKhFN7DihYTg=/0x0:1600x894/fit-in/912x510/https://onyo.s3.amazonaws.com/picture/0d1516c3cd0a4dbcb3c65c92db97aa0f.jpg", "width":1600], ["context": "company-main", "height":894, "url": "http://images.onyo.com/JqgeR-gdLKqa-jydKhFN7DihYTg=/0x0:1600x894/fit-in/912x510/https://onyo.s3.amazonaws.com/picture/0d1516c3cd0a4dbcb3c65c92db97aa0f.jpg", "width":1600]]]

    let validCategoryDict: [String: AnyObject] = ["numericalId":57, "name": "Baked Kids", "image": [["context": "company-main", "height":894, "url": "http://images.onyo.com/BNuPRNzNqmc1Q3VMMUpwSsLt-Pc=/0x52:450x532/fit-in/450x480/https://onyo.s3.amazonaws.com/picture/7156d4e5b028490f9acd382ef3d6d5e1.png", "width":1600]]]
    
    override func setUp() {
        super.setUp()
    }
    
    override func tearDown() {
        super.tearDown()
    }
    
    
    // MARK: - Data Tests
    
    func testCreateCompanyWithDict() {
        var company: Company?
        XCTAssertNil(company, "Not populated yet")
        company = Company(dict: validCompanyDict)
        XCTAssertNotNil(company, "Object User created")
        XCTAssertTrue(company?.numericalId == validCompanyDict["numericalId"] as? Double, "Company Numerical Id")
        XCTAssertTrue(company?.displayName == validCompanyDict["displayName"] as? String, "Company Display Name")
        XCTAssertTrue(company?.address == validCompanyDict["address"] as? String, "Company Address")
        XCTAssertTrue(company?.addressLatitude.value == Double((validCompanyDict["geoLat"] as? String)!), "Company latitude")
        XCTAssertTrue(company?.addressLongitude.value == Double((validCompanyDict["geoLon"] as? String)!), "Company Longitude")
        XCTAssertNotNil(company?.imageMainURL, "Company image")
    }
    
    func testCreateCategoryWithDict() {
        var category: Onyo_challenge.Category?
        XCTAssertNil(category, "Not populated yet")
        category = Category(dict: validCategoryDict)
        XCTAssertNotNil(category, "Object User created")
        XCTAssertTrue(category?.numericalId == validCategoryDict["numericalId"] as? Double, "Category Numerical Id")
        XCTAssertTrue(category?.displayName == validCategoryDict["name"] as? String, "Category Name")
        XCTAssertNotNil(category?.imageMainURL, "Category image")
    }
    
    // MARK: - API Tests
    
    func testCompanyAPIRequest() {
        let expectation = expectationWithDescription("Testing company & categories loading")
        
        OnyoAPIManager.sharedInstance.fetchCompanyList({ (companies, categories) in
            XCTAssertTrue(companies.count > 0, "No company to load")
            XCTAssertTrue(categories.count > 0, "No category to load")
            expectation.fulfill()
        }) { (error) in
            XCTFail("Load company failed with error: " + error.description)
        }
        
        waitForExpectationsWithTimeout(10.0, handler: { error in XCTAssertNil(error, "Testing company & categories failed with error: " + (error?.description)!)})
    }
    
    // MARK: - Realm tests
    
    func testRealmInsertionDeletion() {
        let realm = try! Realm()
        realm.beginWrite()
        realm.deleteAll()
        try! realm.commitWrite()
        
        var companies = Company.companiesFromRealm()
        var categories = Category.categoriesFromRealm()
        
        XCTAssertEqual(companies.count, 0, "No Companies yet");
        XCTAssertEqual(categories.count, 0, "No Categories yet");
        
        let company = Company(dict: validCompanyDict)
        company.save()
        let category = Category(dict: validCategoryDict)
        category.save()
        
        companies = Company.companiesFromRealm()
        categories = Category.categoriesFromRealm()
        
        XCTAssertEqual(companies.count, 1, "Company saved");
        XCTAssertEqual(categories.count, 1, "Categories saved");
        
        realm.beginWrite()
        realm.deleteAll()
        try! realm.commitWrite()
        
        companies = Company.companiesFromRealm()
        categories = Category.categoriesFromRealm()
        
        XCTAssertEqual(companies.count, 0, "Company deleted");
        XCTAssertEqual(categories.count, 0, "Categories deleted");
    }
    
}
