//
//  Category.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import RealmSwift

class Category: Object {
    
    // MARK: - Properties
    
    var numericalId: Double!
    dynamic var displayName: String?
    dynamic var imageMainURL: String?
    
    // MARK: Initialization
    
    convenience init(dict: [String: AnyObject]) {
        self.init()
        
        numericalId = dict["numericalId"] as! Double
        
        displayName = dict["name"] as? String
        
        if let imageArray = dict["image"] as? [[String: AnyObject]] {
            imageMainURL = imageArray[0]["url"] as? String
        }
    }
    
    // MARK: Realm Managers
    
    func save() {
        let realm = try! Realm()
        try! realm.write {
            realm.add(self)
        }
    }
    
    static func categoriesFromRealm() -> [Category] {
        let realm = try! Realm()
        let categories = realm.objects(Category)
        return Array(categories)
    }
    
}