//
//  OnyoAPIManager.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import Alamofire
import UIKit

typealias SuccessHandler = (companies: [Company], categories: [Category]) -> Void
typealias ErrorHandler = (error: NSError!) -> Void

class OnyoAPIManager {
    
    // MARK: - Properties
    
    var useBakedPotatoURL = true
    
    // MARK: - Singleton
    
    class var sharedInstance: OnyoAPIManager {
        struct Static {
            static var instance: OnyoAPIManager?
            static var token: dispatch_once_t = 0
        }
        
        dispatch_once(&Static.token) {
            Static.instance = OnyoAPIManager()
        }
        
        return Static.instance!
    }
    
    private init() {}
    
    // MARK: - Requisitions
    
    func fetchCompanyList(success: SuccessHandler, failure: ErrorHandler) {
        Alamofire.request(.GET, companyURI(), parameters: nil, encoding:.JSON).responseJSON
            { response in switch response.result {
            case .Success(let response):
                var companiesList = [Company]()
                var categoriesList = [Category]()
                
                let companiesReturned = response["companies"] as! [[String: AnyObject]]
                for company in companiesReturned {
                    let company = Company(dict: company)
                    companiesList.append(company)
                }
                
                let categoriesReturned = response["categories"] as! [[String: AnyObject]]
                for category in categoriesReturned {
                    let category = Category(dict: category)
                    categoriesList.append(category)
                }

                success(companies: companiesList, categories: categoriesList)
            case .Failure(let error):
                print("Request failed with error: \(error)")
                failure(error: error)
            }
        }
    }
    
    // MARK: - URL Building
    
    private func companyURI() -> String {
        let path = NSBundle.mainBundle().pathForResource("URIs", ofType: "plist")
        let urls = NSDictionary(contentsOfFile: path!)
        
        var baseURL: String!
        if useBakedPotatoURL {
            baseURL = urls?.objectForKey("BAKED_POTATO_COMPANY_URI") as! String!
        } else {
            baseURL = urls?.objectForKey("GULA_GULA_COMPANY_URI") as! String!
        }
        
        return baseURL
    }
}