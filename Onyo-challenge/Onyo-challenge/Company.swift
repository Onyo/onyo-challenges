//
//  Company.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import MapKit
import RealmSwift

internal class Company: Object {
    
    // MARK: - Properties
    
    var numericalId: Double!
    dynamic var displayName: String?
    dynamic var address: String?
    dynamic var imageMainURL: String?
    
    var addressLatitude = RealmOptional<Double>()
    var addressLongitude = RealmOptional<Double>()
    
    // MARK: Initialization
    
    convenience init(dict: [String: AnyObject]) {
        self.init()
        
        numericalId = dict["numericalId"] as! Double
        
        displayName = dict["displayName"] as? String
        address = dict["address"] as? String
        
        if let imageArray = dict["image"] as? [[String: AnyObject]] {
            if imageArray.count > 2 {
                imageMainURL = imageArray[2]["url"] as? String
            }
        }
        
        if let geoLat = dict["geoLat"] as? String, let geoLon = dict["geoLon"] as? String {
            addressLatitude.value = Double(geoLat)
            addressLongitude.value = Double(geoLon)
        }
    }
    
    // MARK: Realm Managers
    
    func save() {
        let realm = try! Realm()
        try! realm.write {
            realm.add(self)
        }
    }
    
    static func companiesFromRealm() -> [Company] {
        let realm = try! Realm()
        let companies = realm.objects(Company)
        return Array(companies)
    }
    
}